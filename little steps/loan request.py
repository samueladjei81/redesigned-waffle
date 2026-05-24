def main():
    while True:
        credit_score = int(input("Enter your credit score (0 to 10 inclusive): "))
        address_term = int(input("Enter months at present address: "))
        income = float(input("Enter your income (£s): "))
        loan_request = float(input("Enter the loan request (£s): "))

        if (credit_score == 0 or income == 0 or address_term < 12):
            result = "Loan request refused"
        elif (
            credit_score >= 7
            and 12 < address_term < 60
            and loan_request <= income
        ):
            result = "Loan granted"
        elif (
            2 <= credit_score <= 5
            and address_term >= 60
            and loan_request <= income
        ):
            result = "Loan granted"
        elif (
            credit_score == 1
            and address_term > 12
            and loan_request <= 0.2 * income
        ):
            result = "Loan granted"
        elif (
            income >= loan_request
            and 2 * income >= loan_request
            and address_term >= 60
            and credit_score >= 5
        ):
            result = "Loan granted"
        else:
            result = "Loan request refused"

        print(f"Credit Score: {credit_score}")
        print(f"Address Term (months): {address_term}")
        print(f"Income (£s): {income}")
        print(f"Loan Request (£s): {loan_request}")
        print(f"Loan Decision: {result}")

        another_loan = input("Do you want to process another loan application? (yes/no): ")
        if another_loan.lower() != "yes":
            break

if __name__ == "__main__":
    main()
