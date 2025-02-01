import csv

# Input CSV file
csv_file = 'faq.csv'
# Output HTML file
html_file = 'faq.html'

# Read the CSV file and convert it to an HTML table
with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Read the header row

    # Start creating the HTML content
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>GrocerEase FAQ</title>
    </head>
    <body>
        <h1>GrocerEase FAQ</h1>
        <table border="1">
            <tr>
    '''
    
    # Add headers to the HTML table
    for header in headers:
        html_content += f'<th>{header}</th>'
    html_content += '</tr>'
    
    # Add rows to the HTML table
    for row in csv_reader:
        html_content += '<tr>'
        for cell in row:
            html_content += f'<td>{cell}</td>'
        html_content += '</tr>'
    
    # Close the HTML content
    html_content += '''
        </table>
    </body>
    </html>
    '''
    
    # Write the HTML content to a file
    with open(html_file, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)

print(f"HTML file '{html_file}' has been created successfully!")