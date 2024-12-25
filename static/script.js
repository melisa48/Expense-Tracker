document.addEventListener('DOMContentLoaded', function() {
     fetch('/api/expenses')
         .then(response => response.json())
         .then(data => {
             // Process data for chart (e.g., group by category)
             const categories = {};
             data.forEach(expense => {
                 if (categories[expense.category]) {
                     categories[expense.category] += expense.amount;
                 } else {
                     categories[expense.category] = expense.amount;
                 }
             });
 
             // Clear existing chart
             const chart = document.getElementById('expense-chart');
             chart.innerHTML = '<h3>Expenses by Category</h3>';
 
             // Create a more visually appealing bar chart
             Object.entries(categories).forEach(([category, amount]) => {
                 const barContainer = document.createElement('div');
                 barContainer.style.marginBottom = '10px';
                 barContainer.style.display = 'flex';
                 barContainer.style.alignItems = 'center';
 
                 const label = document.createElement('span');
                 label.textContent = `${category}: `;
                 label.style.minWidth = '100px';
                 barContainer.appendChild(label);
 
                 const bar = document.createElement('div');
                 const maxWidth = 300; // Maximum width of the bar
                 const width = Math.min((amount / Object.values(categories).reduce((a, b) => a + b)) * maxWidth, maxWidth);
                 bar.style.width = `${width}px`;
                 bar.style.height = '20px';
                 bar.style.backgroundColor = 'blue';
                 bar.style.marginRight = '10px';
                 barContainer.appendChild(bar);
 
                 const amountLabel = document.createElement('span');
                 amountLabel.textContent = `$${amount.toFixed(2)}`;
                 barContainer.appendChild(amountLabel);
 
                 chart.appendChild(barContainer);
             });
         });
 });
 