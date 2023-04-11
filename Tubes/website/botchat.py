from flask import Blueprint, render_template,request
import openai
botchats = Blueprint('botchat',__name__)
openai.api_key = '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'
@botchats.route('/botchat', methods = ['GET', 'POST'])
def botchat():
    if request.method == 'POST':
        input_text = request.form['input_text']
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Respon yang tepat untuk curhatan ini adalah: {input_text}. Kata-kata yang mungkin cocok untuk respon adalah:",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        recommended_text = response.choices[0].text
        return render_template('botchat.html', input_text=input_text, recommended_text=recommended_text)
    else:
        return render_template('botchat.html')
    
