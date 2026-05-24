#write a code for how many m/s make up 1km/hr
#km_per_hr = 1000m/3600s
#1km/hr = 10m/36s
#1km/hr = 0.277778 m/s
#let 1km/hr == a
# therefore 1a = 0.277778 m/s
# therefore 2a = 2 * 0.277778 m/s
#initialize km_per_hr
km_per_hr = int(input('how many km/h?:'))
#compare km_per_hr and m_per_s
m_per_s = km_per_hr * 0.277778
km_per_hr = m_per_s / 0.277778
#convert to m/s
print(m_per_s,'m/s')
