from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML strings for the login and success pages
index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Awinfo Hub</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #000428; /* Dark Blue Gradient */
            background-image: linear-gradient(to right, #000428, #004e92); /* Dark and Deep Sky Blue */
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            position: relative;
        }

        .container {
            text-align: center;
            padding: 20px;
            border-radius: 15px;
            background-color: rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
        }

        .top-left-image {
            position: absolute;
            top: 10px;
            left: 10px;
            height: 100px; /* Logo height */
        }

        h1 {
            font-size: 3rem;
            margin-bottom: 20px;
            color: #00c6ff; /* Deep Sky Blue */
        }

        .login-form {
            margin-top: 20px;
        }

        .login-form input {
            width: 80%;
            padding: 10px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
        }

        .login-form input[type="text"],
        .login-form input[type="password"] {
            background-color: #001f3f; /* Dark Blue */
            color: #ffffff;
        }

        .login-form button {
            padding: 10px 20px;
            font-size: 1.2rem;
            border: none;
            border-radius: 5px;
            background-color: #00c6ff; /* Deep Sky Blue */
            color: #000428;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .login-form button:hover {
            background-color: #0086b3; /* Slightly darker sky blue */
        }

        .title {
            animation: fade-in 2s;
        }

        @keyframes fade-in {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .footer {
            margin-top: 20px;
            font-size: 0.9rem;
            color: #dddddd;
        }

        .footer a {
            color: #00c6ff;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <!-- Replace 'your-logo-url' with your logo image URL -->
    <img src="Awinfo.png" alt="Logo" class="top-left-image">
    
    <div class="container">
        <h1 class="title">Awinfo Hub</h1>
        <p>Welcome to Awinfo Hub. Please login to continue.</p>
        
        <form class="login-form" method="POST">
            <input type="text" name="email" placeholder="Email" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        
        <div class="footer">
            <p>Forgot your password? <a href="#">Click here</a></p>
        </div>
    </div>
</body>
</html>
"""

success_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Successful</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #ffffff;
            text-align: center;
            padding: 50px;
        }

        h1 {
            font-size: 2rem;
            color: #00c6ff;
        }

        .circle-loader {
            position: relative;
            display: inline-block;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            border: 5px solid #00c6ff;
            border-top: 5px solid transparent;
            animation: spin 2s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .checkmark {
            position: absolute;
            top: 15px;
            left: 15px;
            width: 70px;
            height: 70px;
            border: 5px solid #00c6ff;
            border-radius: 50%;
            background-color: white;
            animation: checkmark 1s ease-out forwards;
        }

        @keyframes checkmark {
            0% { transform: scale(0); opacity: 0; }
            50% { transform: scale(1.1); opacity: 1; }
            100% { transform: scale(1); opacity: 1; }
        }
    </style>
</head>
<body>
    <h1>Login Successful! Welcome to Awinfo Hub</h1>
    <div class="circle-loader">
        <div class="checkmark"></div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # When the form is submitted
        email = request.form['email']  # Captures the email entered in the form
        password = request.form['password']  # Captures the password entered in the form
        
        # Now you have the user's email and password
        print(f"Email: {email}, Password: {password}")  # Prints to the console (terminal)
        
        # You can also redirect the user to a different page or show a message
        return render_template_string(success_html)  # Render success page after login

    # If the method is GET, it will simply render the login page
    return render_template_string(index_html)  # Return the login page as a string

if __name__ == "__main__":
    app.run(debug=True)
