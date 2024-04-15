import os

def generate_invoice_html(user_input):
    base_url = "file://{}".format(os.path.abspath("invoice_style.html"))
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{base_url}">
</head>
<body>
    <div class="invoice-container">
        <h1 class="invoice-title">Gym Invoice</h1>
        <div class="invoice-details">
            <p><strong>Gym Plan:</strong> {user_input['gym_plan']}</p>
            <p><strong>Membership Duration:</strong> {user_input['membership_duration']} months</p>
            {generate_personal_trainer_details(user_input['personal_trainer'])}
        </div>
    </div>
</body>
</html>
"""

def generate_personal_trainer_details(personal_trainer):
    if personal_trainer:
        return """
        <p><strong>Personal Trainer:</strong> Included</p>
        """
    else:
        return """
        <p><strong>Personal Trainer:</strong> Not Included</p>
        """
