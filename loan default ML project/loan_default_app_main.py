import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Set up session state to control navigation
if "page" not in st.session_state:
    st.session_state.page = "start"

def go_to_main():
    st.session_state.page = "main"

# Load the model
model = pickle.load(open("xgboost_model.pkl", "rb"))

# ---- PAGE STYLE (CSS) ----
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
            color: white;
        }
        .top-right {
            position: absolute;
            top: 10px;
            right: 20px;
            font-size: 1.2em;
            font-weight: bold;
            color: #ffcc00;
        }
        h1 {
            text-align: center;
            color: #ffcc00;
            font-size: 2.5em;
            text-shadow: 2px 2px 5px rgba(255, 255, 255, 0.3);
        }
        .stNumberInput input, .stSelectbox select {
            background: #1e3c72;
            color: white;
            border-radius: 10px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ffcc00, #ff6600);
            color: black;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #ff6600, #ffcc00);
            transform: scale(1.05);
        }
        .result-card {
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-size: 1.3em;
            font-weight: bold;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# ---- PAGE ROUTING ----
if st.session_state.page == "start":
    st.markdown("""
        <div style='text-align: center; padding: 100px 20px;'>
            <h1 style='font-size: 3em; color: #ffcc00;'>🔍 Welcome to the Loan Default Risk Predictor</h1>
            <p style='font-size: 1.3em; color: white; max-width: 700px; margin: 20px auto;'>
                This intelligent tool helps financial institutions assess the likelihood of loan default using machine learning. 
                Click below to begin the risk evaluation process.
            </p>
            <br>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Get Started"):
        go_to_main()

elif st.session_state.page == "main":
    st.markdown("<div class='top-right'>ID: D3000623</div>", unsafe_allow_html=True)
    st.markdown("<h1>📊 Loan Default Likelihood App</h1>", unsafe_allow_html=True)
    st.markdown("---")

    with st.container():
        st.markdown("### 📝 Enter Loan Applicant Details:")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            input_fields_1 = {
                'Age': st.number_input('🎂 Age*', min_value=18, max_value=100, value=30),
                'Income': st.number_input('💰 Income ($)*', min_value=0, value=50000),
                'LoanAmount': st.number_input('🏦 Loan Amount ($)*', min_value=0, value=100000),
                'CreditScore': st.number_input('🔢 Credit Score', min_value=300, max_value=850, value=650)
            }

        with col2:
            input_fields_2 = {    
                'MonthsEmployed': st.number_input('🗓️ Months Employed*', min_value=0, value=12),
                'NumCreditLines': st.number_input('🏦 Number of Credit Lines', min_value=0, value=3),
                'InterestRate': st.number_input('📈 Interest Rate (%)*', min_value=0.0, value=5.0, format="%.2f"),
                'LoanTerm': st.number_input('📆 Loan Term (Months)', min_value=1, value=36)
            }

        with col3:
            input_fields_3 = {
                'DTIRatio': st.number_input('⚖️ Debt-to-Income Ratio', min_value=0.0, max_value=1.0, value=0.3, format="%.2f"),
                'Education': st.selectbox('🎓 Education Level', ["Bachelor's", 'High School', "Master's", 'PhD']),
                'EmploymentType': st.selectbox('💼 Employment Type*', ['Full-time', 'Part-time', 'Self-employed', 'Unemployed']),
                'MaritalStatus': st.selectbox('💍 Marital Status*', ['Divorced', 'Married', 'Single'])
            }

        with col4:
            input_fields_4 = {
                'HasMortgage': st.selectbox('🏠 Has Mortgage?*', ['Yes', 'No']),
                'HasDependents': st.selectbox('👨‍👩‍👧 Has Dependents?*', ['Yes', 'No']),
                'LoanPurpose': st.selectbox('🎯 Loan Purpose', ['Auto', 'Business', 'Education', 'Home', 'Other']),
                'HasCoSigner': st.selectbox('🤝 Has Co-Signer?*', ['Yes', 'No'])
            }

    st.markdown("---")

    submit = st.button('🚀 Submit Application')

    if submit:
        loan_default = pd.read_csv('Loan_default1.csv')
        loan_default.drop('LoanID', axis=1, inplace=True)
        loan_default_n = loan_default.copy()

        ordinal_cols = ['Education', 'HasDependents', 'HasMortgage', 'HasCoSigner', 'MaritalStatus', 'LoanPurpose', 'EmploymentType']
        label_encoders = {}

        for col in ordinal_cols:
            label_encoder = LabelEncoder()
            loan_default_n[col] = label_encoder.fit_transform(loan_default_n[col])
            label_encoders[col] = label_encoder

        numeric_features = loan_default_n.select_dtypes(include=['number']).columns.drop('Default', errors='ignore')
        scaler = MinMaxScaler()
        loan_default_n[numeric_features] = scaler.fit_transform(loan_default_n[numeric_features])

        concatenated_fields = {**input_fields_1, **input_fields_2, **input_fields_3, **input_fields_4}
        new_data = pd.DataFrame([concatenated_fields])

        for col in ordinal_cols:
            if col in new_data:
                if new_data[col].iloc[0] in label_encoders[col].classes_:
                    new_data[col] = label_encoders[col].transform(new_data[col])
                else:
                    new_data[col] = label_encoders[col].transform([label_encoders[col].classes_[0]])[0]

        new_data[numeric_features] = scaler.transform(new_data[numeric_features])

        prediction = model.predict(new_data)

        st.markdown("---")

        if prediction[0] == 1:
            st.markdown(
                "<div class='result-card' style='background: linear-gradient(135deg, #ff4c4c, #ff0000); color: white;'>"
                "<h2>⚠️ High Risk of Default! </h2>"
                "<p>This applicant is likely to default on the loan.</p>"
                "</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='result-card' style='background: linear-gradient(135deg, #4CAF50, #2E8B57); color: white;'>"
                "<h2>✅ Low Risk of Default </h2>"
                "<p>This applicant is unlikely to default on the loan.</p>"
                "</div>",
                unsafe_allow_html=True
            )
