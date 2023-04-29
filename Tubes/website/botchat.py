from flask import Blueprint, render_template,request
import openai
botchats = Blueprint('botchat',__name__)
openai.api_key = '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'
@botchats.route('/botchat', methods = ['GET', 'POST'])
def botchat():
    if request.method == 'POST':
        input_text = request.form['input_text']
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"""Bertindak sebagai psikolog, beri respon untuk curhatan dengan benar dan sopan. Berikan saran yang tidak akan membuat user semakin sakit hati dan sedih. Jika user meminta sesuatu usahakan kamu dapat memberikan yang diminta user dan membantu menyelesaikan masalah yang ditanyakan (baik dalam kata kata ataupun bentuk lain)
            User :{input_text}
            AI :
            """,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5,
        )
        recommended_text = response.choices[0].text
        return render_template('botchat.html', input_text=input_text, recommended_text=recommended_text)
    else:
        return render_template('botchat.html')
    
