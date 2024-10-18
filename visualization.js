// visualization.js

// Function to Get Query Parameter from the URL
function getQueryParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
}

// Get the Selected Dataset from the Query Parameter
const datasetName = getQueryParam("dataset");
const datasetDisplay = document.getElementById("datasetName");
const chartCanvas = document.getElementById("chart");
let chartInstance = null; // Store chart instance to manage updates

// Sample Data for Visualization (Replace with real data or dynamic loading logic)
const sampleData = {
    "testing_merge.csv": {
        labels: ["District A", "District B", "District C", "District D"],
        data: [120, 200, 300, 250],
        chartType: "bar"
    },
    "PropertyTax_DataSet_2019-20_to_2023-24_20240421_V1.xlsx": {
        labels: ["2019", "2020", "2021", "2022", "2023"],
        data: [5000, 5200, 5400, 5600, 5800],
        chartType: "line"
    },
    "school-districts_lea_directory.csv": {
        labels: ["Elementary", "High School", "Unified", "Other"],
        data: [50, 30, 20, 10],
        chartType: "pie"
    }
};

// Display the Selected Dataset Name or an Error Message
if (datasetName && sampleData[datasetName]) {
    datasetDisplay.textContent = `Visualizing: ${datasetName}`;
    const datasetInfo = sampleData[datasetName];

    // Render the Chart
    renderChart(datasetInfo.labels, datasetInfo.data, datasetInfo.chartType);
} else {
    datasetDisplay.textContent = "No valid dataset selected or data unavailable.";
}

// Function to Render the Chart using Chart.js
function renderChart(labels, data, type) {
    if (chartInstance) {
        chartInstance.destroy(); // Destroy existing chart if any
    }

    chartInstance = new Chart(chartCanvas, {
        type: type,
        data: {
            labels: labels,
            datasets: [{
                label: "Dataset Visualization",
                data: data,
                backgroundColor: [
                    "rgba(75, 192, 192, 0.5)",
                    "rgba(255, 99, 132, 0.5)",
                    "rgba(54, 162, 235, 0.5)",
                    "rgba(255, 206, 86, 0.5)"
                ],
                borderColor: [
                    "rgba(75, 192, 192, 1)",
                    "rgba(255, 99, 132, 1)",
                    "rgba(54, 162, 235, 1)",
                    "rgba(255, 206, 86, 1)"
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: "top"
                },
                title: {
                    display: true,
                    text: "Dataset Visualization"
                }
            }
        }
    });
}
