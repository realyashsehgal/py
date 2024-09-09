import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_plot():
    # Sample data
    labels = ['Income', 'Expenses']
    values = [5000, 3000]

    # Create a bar plot
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['blue', 'red'])
    plt.title('Income vs Expenses')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    
    # Save the plot as an image
    plt.savefig('plot.png')
    plt.close()

def create_pdf_with_plot(file_name):
    # Create the PDF
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Add title and summary text
    c.drawString(100, height - 100, "Personal Finance Report")
    c.drawString(100, height - 150, "Summary of Your Financial Data:")
    c.drawString(100, height - 200, "Total Income: $5000")
    c.drawString(100, height - 220, "Total Expenses: $3000")

    # Add plot image to the PDF
    c.drawImage('plot.png', 100, height - 400, width=400, height=200)
    
    # Save the PDF
    c.save()

# Generate the plot
create_plot()

# Create the PDF with the plot
create_pdf_with_plot("finance_report_with_plot.pdf")
