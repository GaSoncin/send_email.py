import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox


def send_email(subject, body, to_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = ""
    smtp_password = ""

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())
        server.quit()
        messagebox.showinfo("Sucesso", "Email enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar email: {e}")


def on_send():
    subject = entry_subject.get()
    body = text_body.get("1.0", tk.END)
    to_email = entry_to.get()
    send_email(subject, body, to_email)


root = tk.Tk()
root.title("Envio de Emails")

tk.Label(root, text="Para:").grid(row=0, column=0)
entry_to = tk.Entry(root, width=50)
entry_to.grid(row=0, column=1)

tk.Label(root, text="Assunto:").grid(row=1, column=0)
entry_subject = tk.Entry(root, width=50)
entry_subject.grid(row=1, column=1)

tk.Label(root, text="Corpo do Email:").grid(row=2, column=0)
text_body = tk.Text(root, height=10, width=50)
text_body.grid(row=2, column=1)

btn_send = tk.Button(root, text="Enviar", command=on_send)
btn_send.grid(row=3, column=1)

root.mainloop()