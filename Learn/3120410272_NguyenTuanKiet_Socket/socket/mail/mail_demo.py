# Chức năng chính : Gửi email từ một địa chỉ email đến một địa chỉ email khác thông qua SMTP

import smtplib, ssl

port = 465

sender = 's_abc@gmail.com'
receiver = 'r_abc@gmail.com'

password = input('Enter password: ')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.starttls()
    
    server.login(sender, password)
    
    server.sendmail(sender, receiver, 'Nội dung được gửi từ SGU.COM'.encode('utf-8'))
    
    print('Gửi thành công!')
