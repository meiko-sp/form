import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from gitdb.util import hex_to_bin

# Streamlit UI
st.title("材料管理アプリ設定手順")

st.write("""
※AppSheet、SlackともにGoogleアカウントが必要です。

Googleアカウントは普段使わないようなアカウントが好ましいと思います。

## インストール

2つのアプリをスマホにインストールして下さい。

- AppSheet  
- Slack

""")

images = ["image/appsheet.png", "image/slack.png"]
st.image(images, caption=["AppSheet", "slack"], width=100)

st.write("""

2つとも無料でインストールできます。

## 使用するGmailを教えてください。

インストールが完了したら、以下の欄にGmailアドレスを入力してください。

""")

email = st.text_input("koumu2377@gmail.comからメールが届くだけです。")

pass_word = st.text_input("パスワードを入力してください。")


if st.button("送信"):
    if email:
        try:
            sender_email = "koumu2377@gmail.com"  # 送信元のメールアドレス
            sender_password = pass_word       # 送信元メールアドレスのパスワード
            subject = "招待メール"
            body = f"""{email} さん
            
            入力したGmailアドレスあてにAppSheetとSlackの招待メールを送信します。
            しばらくお待ちください。
            
            片山
            """

            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = email
            msg["Cc"] = "koumu08@meiko-sp.com"
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # SMTP接続
            server = smtplib.SMTP("smtp.gmail.com", 587)  # SMTPサーバーを適切なものに変更
            server.starttls()
            server.login(sender_email, sender_password)

            recipients = [email, "koumu08@meiko-sp.com"]
            server.sendmail(sender_email, recipients, msg.as_string())
            server.quit()

            st.success("メールを送信しました！")
        except Exception as e:
            st.error(f"メール送信に失敗しました: {e}")
    else:
        st.warning("メールアドレスを入力してください。")

st.write("""
問題があれば片山まで教えてください。

## 事前に設定してほしいこと

Slackの通知はオンにしてください。気付かないので。

## 簡単な使い方説明

""")

st.write("簡単な説明だけなので分からなければ聞いてください。")

width = 500

st.write("右上のRegistを押して下さい。")
st.image("image/1.png")

st.write("重量を入力します。")
st.image("image/2.png", width=width)

st.write("ステータスが確認待ちになります。")
st.image("image/3.png", width=width)

st.write("Slackに通知がきます。")
st.image("image/4.png")

st.write("材料を確認した人がチェックマークを押します。確認待ちが確認済みになります。")
st.image("image/5.png", width=width)


st.write("""

チェックをしないと通知が止まらないようになっています。
指定した時間（10分）を超えても止まらない場合は、責任者が確認を取ってください。

""")

st.image("image/6.png", caption="天候で制限時間は変わるようになっています。" ,width=400)
