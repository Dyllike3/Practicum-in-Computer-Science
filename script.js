// script.js

// List of Datasets (Add your datasets here)
const datasets = [
    {
        name: "Property Tax Data (2019-20 to 2023-24)",
        file: "PropertyTax_DataSet_2019-20_to_2023-24_20240421_V1.xlsx"
    },
    {
        name: "Property Tax Data (2019-05-13)",
        file: "PropertyTax_DataSet_20190513.xlsx"
    },
    {
        name: "Testing Merge (CSV)",
        file: "testing_merge.csv"
    },
    {
        name: "Testing Merge (CA State Controller)",
        file: "testing_merge_ca_state_cont.csv"
    },
    {
        name: "School Districts LEA Directory (CSV)",
        file: "school-districts_lea_directory.csv"
    },
    {
        name: "All Datasets (ZIP)",
        file: "Data.zip"
    }
];

// Handle Search Form Submission
document.getElementById('searchForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form refresh

    const query = document.getElementById('searchInput').value.toLowerCase().trim();
    const results = datasets.filter(dataset =>
        dataset.name.toLowerCase().includes(query)
    );

    displaySearchResults(results);
});

// Function to Display Search Results
function displaySearchResults(results) {
    const searchResults = document.getElementById('searchResults');
    searchResults.innerHTML = ""; // Clear previous results

    if (results.length === 0) {
        searchResults.innerHTML = "<p>No matching datasets found.</p>";
    } else {
        const ul = document.createElement('ul'); // Create a list for results

        results.forEach(dataset => {
            // Create a list item for download
            const downloadLi = document.createElement('li');
            downloadLi.innerHTML = `
                <a href="datasets/${dataset.file}" download class="download-link">
                    Download ${dataset.name}
                </a>
            `;
            ul.appendChild(downloadLi);

            // Create a list item for visualization
            const visualizeLi = document.createElement('li');
            visualizeLi.innerHTML = `
                <a href="visualization.html?dataset=${dataset.file}" class="download-link">
                    Visualize ${dataset.name}
                </a>
            `;
            ul.appendChild(visualizeLi);
        });

        searchResults.appendChild(ul); // Append the results to the search container
    }
}
