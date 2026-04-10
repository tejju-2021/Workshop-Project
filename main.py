from flask import Flask,request,jsonify,send_from_directory

app=Flask(__name__)
def chatbot(user_input):
    user_input = user_input.lower()

    if user_input == "bye":
        return "Goodbye! Have a Nice Day 😊"

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    elif "location" in user_input:
        return "📍Sector 82, NH-64, Near Power Plant, Noida, Uttar Pradesh"

    elif "appointment" in user_input:
        return "Please provide your details: Name, Age, Symptoms, Date & Time"

    elif "help" in user_input or "emergency" in user_input:
        return "Don't Panic! Call 18001223455"

    elif "ambulance" in user_input:
        return "Call 108 for Ambulance 🚑"

    elif "order" in user_input:
        return "Mail your address & medicines to hospi.tal@gmail.com"

    elif "services" in user_input:
        return "We provide Appointment, Ambulance, Emergency & Medicine Delivery services."

    elif "doctor" in user_input:
        return "Which specialist? (heart / stomach / general)"

    elif "heart" in user_input:
        return "Contact Cardiologist: 18002452554"

    elif "stomach" in user_input:
        return "Contact Gastroenterologist: 18542549798"

    elif "symptom" in user_input:
        return "Please describe your symptoms."

    elif "fever" in user_input or "cold" in user_input:
        return "Consult a General Physician 🩺"

    elif "chest pain" in user_input:
        return "Consult a Cardiologist immediately 🫀"

    elif "fracture" in user_input:
        return "Consult an Orthopedic Doctor 🦴"

    elif "lab" in user_input or "test" in user_input:
        return "We provide Blood test, MRI, CT Scan. Reports in 24 hrs."

    elif "fees" in user_input or "fee" in user_input:
        return "Consultation fee is ₹500"

    else:
        return "Sorry 😓, I didn't understand"

@app.route("/")
def home():
    return send_from_directory('.','webpage.html')
@app.route("/home.html")
def home_page():
    return send_from_directory('.', 'home.html')

@app.route("/about.html")
def about_page():
    return send_from_directory('.', 'about.html')

@app.route("/form.html")
def form_page():
    return send_from_directory('.', 'form.html')

@app.route("/chat",methods=["POST"])
def chat():
    data=request.json
    user_message=data.get("message")
    response=chatbot(user_message)
    return jsonify({"response": response})

if __name__ =="__main__":
    print("Chatbot is running! Visit http://127.0.0.1:5000 in your browser")
    print("Serving homepage.html file")
    app.run(debug=True)
    