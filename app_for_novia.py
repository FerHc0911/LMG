from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>💖 Gracias por todo, mi amor 💖</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500&display=swap');
        
        body {
            background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%);
            font-family: 'Quicksand', sans-serif;
            text-align: center;
            color: #fff;
            margin-top: 40px;
            overflow: hidden;
        }

        h1 {
            font-family: 'Great Vibes', cursive;
            font-size: 3em;
            color: #fff;
            text-shadow: 2px 2px 10px rgba(255, 192, 203, 0.8);
            animation: fadeInDown 2s ease;
        }

        .mensaje {
            font-size: 1.3em;
            background-color: rgba(255, 255, 255, 0.15);
            padding: 25px;
            border-radius: 20px;
            width: 80%;
            margin: 40px auto;
            line-height: 1.6;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
            animation: fadeIn 3s ease;
        }

        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .hearts {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: -1;
        }

        .heart {
            position: absolute;
            color: #ffb6c1;
            animation: floatHearts 6s linear infinite;
        }

        @keyframes floatHearts {
            0% { transform: translateY(100vh) scale(0.5); opacity: 0.7; }
            100% { transform: translateY(-10vh) scale(1); opacity: 0; }
        }

        footer {
            margin-top: 40px;
            font-size: 1em;
            opacity: 0.9;
        }
    </style>
</head>
<body>
    <div class="hearts">
        {% for i in range(20) %}
            <div class="heart" style="left:{{ (i*5)%100 }}%; animation-delay: {{ i*0.5 }}s;">💖</div>
        {% endfor %}
    </div>

    <h1>Para ti, mi amor 💞</h1>
    <div class="mensaje">
        🌹 Hoy solo quiero agradecerte por todo este tiempo que hemos estado juntos.  
        Gracias por tu paciencia, por tus sonrisas, por los momentos simples y los inolvidables.  
        Gracias por ser mi apoyo, mi inspiración y mi razón para sonreír cada día.  
        Eres la persona más especial que ha llegado a mi vida, y cada instante a tu lado  
        me confirma lo afortunado que soy de tenerte. 💫  
        <br><br>
        Te amo más de lo que las palabras pueden decir. ❤️
    </div>

    <footer>— Con amor, tuyo por siempre 💌</footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(TEMPLATE)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

