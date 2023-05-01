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
            prompt=f"""Bertindak sebagai psikolog, beri respon untuk curhatan dengan benar dan sopan. Berikan saran yang tidak akan membuat user semakin sakit hati dan sedih. Jika user meminta sesuatu usahakan kamu dapat memberikan yang diminta user dan membantu menyelesaikan masalah yang ditanyakan (baik dalam kata kata ataupun bentuk lain). Buat respon lebih panjang
            User :{input_text}
            AI :
            """,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # Bagian prompt untuk rekomendasi lagu
        response2 = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"""
            Berikut adalah beberapa rekomendasi lagu yang ceria dan bisa meningkatkan mood Anda:Contohnya(kamu dapat memberikan rekomendasi lagu lain yang sesuai dengan mood lagu dibawah ini, sesuaikan juga dengan input user jika user ada memberikan kesukaan lagu user)
            Good Day - IU, Beautiful Day - U2, Happy - Pharrell Williams
            (Hanya pilih 5 lagu untuk user, tidak perlu lebih, buat list lagu dalam nomor 1,2,3 dan seterusnya)
            (1)
            (2)
            (3)
            (4)
            (5)
            Semoga membantu!
            """,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # Bagian prompt untuk kegiatan yang bisa dilakukan oleh user
        response3 = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"""
            Berikut adalah beberapa kegiatan yang bisa membantu Anda merasa lebih baik:(kamu bisa berikan kegiatan kegiatan lain, saya berikan contoh di bawah, kamu bisa ambil dari contoh ataupun bisa mencari kegiatan kegiatan lain). Contoh:
            1. Berjalan-jalan di luar rumah atau taman
            2. Mendengarkan musik favorit Anda
            3. Menonton film lucu atau menghibur
            4. Menulis jurnal atau membuat daftar hal-hal yang membuat Anda bersyukur
            5. Menghubungi teman atau keluarga untuk berbicara atau bertemu
            6. Berlatih yoga atau meditasi untuk meredakan stres
            7. Melakukan hobi atau aktivitas yang disukai
            (Pilihkan user 3  kegiatan  yang bisa dilakukan oleh user untuk membantu user agar tidak sedih ataupun lebih ceria ataupun lebih senang, buatkan jawaban dalam urutan nomor 
            (1)
            (2)
            (3)
            Semoga membantu!
            """,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # Bagian prompt untuk Quote of the Day
        response4 = openai.Completion.create(
            engine="text-davinci-003",
            prompt="""
            Berikut adalah beberapa Quote of the Day yang bisa memotivasi Anda:(quote dibawah hanya sebagai contoh, kamu bisa pilih quote lain yang juga memotivasi, kamu bisa sesuaikan juga dengan user jika user ada preferensi tertentu). Ini hanya sebagai contoh:
            1. "The greatest glory in living lies not in never falling, but in rising every time we fall." - Nelson Mandela
            2. "The only way to do great work is to love what you do." - Steve Jobs
            3. "Believe you can and you're halfway there." - Theodore Roosevelt
            (Pilihkan user 1 Quote of the Day yang memotivasi, kamu bisa pilih random dari sumber lain )
            """,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5,
        )


        recommended_songs = response2.choices[0].text
        recommended_text = response.choices[0].text
        recommended_activities = response3.choices[0].text
        quoteOTD = response4.choices[0].text
        return render_template('botchat.html', input_text=input_text, recommended_songs=recommended_songs,recommended_activities=recommended_activities,quoteOTD=quoteOTD,recommended_text=recommended_text)
    else:
        return render_template('botchat.html')
    
