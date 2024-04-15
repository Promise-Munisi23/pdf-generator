import sys
import invoice_generator
import generate_pdf_from_html

def gather_user_input():
    gym_plan = input("Enter your gym plan (e.g., Basic, Premium): ")
    membership_duration = int(input("Enter the duration of your membership in months: "))
    personal_trainer = input("Do you want a personal trainer? (yes/no): ").lower() == "yes"
    return {
        "gym_plan": gym_plan,
        "membership_duration": membership_duration,
        "personal_trainer": personal_trainer
    }

if __name__ == "__main__":
    user_input = gather_user_input()
    with open("invoice.html", "w") as html_file:
        html_file.write(invoice_generator.generate_invoice_html(user_input))
    generate_pdf_from_html.generate_pdf_from_html("invoice.html", "invoice.pdf")
    print("Invoice has been generated as invoice.pdf")
