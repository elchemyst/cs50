document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('.table tbody tr');
    const footerRow = document.getElementById('footer-row');
    rows.forEach(row => {
        row.addEventListener('mouseover', function() {
            this.classList.add('highlight-row');
        });
        row.addEventListener('mouseout', function() {
            this.classList.remove('highlight-row');
        });
    });
    // if (footerRow) {
    //     setInterval(function() {
    //         footerRow.classList.toggle('blink');
    //     }, 800);
    // }
    function formatAsUSD(number) {
            if (typeof number !== 'number') {
                return number; // Return as is if not a number (e.g., "N/A")
            }
            return new Intl.NumberFormat('en-US', {
                style: 'currency',
                currency: 'USD'
            }).format(number);
    }
    // This function will make the AJAX call and update the page
        async function updatePortfolioPrices() {
            try {
                // 1. Make the AJAX request to our Flask endpoint
                //    'fetch()' is a modern way to make network requests (AJAX).
                //    It returns a Promise (a special JavaScript object for asynchronous operations).
                const response = await fetch('/get_portfolio_data');

                // 2. Check if the request was successful
                if (!response.ok) { // 'ok' is true for 200-299 status codes
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }

                // 3. Parse the JSON response
                //    '.json()' also returns a Promise. 'await' waits for it to finish.
                const data = await response.json();

                // 4. Update the individual stock prices and totals in the table
                data.stocks.forEach(stock => {
                    const priceElement = document.getElementById(`price-${stock.symbol}`);
                    const totalElement = document.getElementById(`total-${stock.symbol}`);

                    if (priceElement) {
                        priceElement.textContent = formatAsUSD(stock.current_price);
                    }
                    if (totalElement) {
                        totalElement.textContent = formatAsUSD(stock.total_stock_value);
                    }
                });

                // 5. Update Cash and Grand Total
                const cashElement = document.getElementById('cash-value');
                const grandTotalElement = document.getElementById('grand-total-value');

                if (cashElement) {
                    cashElement.textContent = formatAsUSD(data.cash);
                }
                if (grandTotalElement) {
                    // Make sure to access the <strong> element inside, or just update the td
                    // If you kept the <strong> inside, you'd target grandTotalElement.querySelector('strong')
                    grandTotalElement.innerHTML = `<strong>${formatAsUSD(data.total_portfolio_value)}</strong>`;
                }


            } catch (error) {
                // 6. Handle any errors during the process
                console.error("Failed to fetch portfolio data:", error);
                // You might want to display a message to the user here
            }
        }

        // --- Start the real-time updates ---

        // Call the function once immediately when the page loads
        updatePortfolioPrices();

        // Then, call it repeatedly every 10 seconds (10000 milliseconds)
        setInterval(updatePortfolioPrices, 10000); // Adjust interval as needed
});
