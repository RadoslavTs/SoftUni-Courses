import smtplib

server = smtplib.SMTP('smtp.abv.bg', 465)
server.login("rado.89", "sdgfJ7*-gjase(-gfd7")
msg = "Баце, пайтън хаква :)"
server.sendmail("r.tsepenishev@gmail.com", "r.tsepenishev@gmail.com", msg)
