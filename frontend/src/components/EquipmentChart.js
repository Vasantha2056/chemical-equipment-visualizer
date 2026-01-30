import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Tooltip, Legend } from "chart.js";
import { useEffect, useState } from "react";

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

function EquipmentChart() {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    fetch("http://localhost:3004/api/equipment")
      .then(res => res.json())
      .then(data => {
        const count = {};

        data.forEach(item => {
          count[item.type] = (count[item.type] || 0) + 1;
        });

        setChartData({
          labels: Object.keys(count),
          datasets: [
            {
              label: "Equipment Count",
              data: Object.values(count),
              backgroundColor: "rgba(75,192,192,0.6)"
            }
          ]
        });
      })
      .catch(err => console.error(err));
  }, []);

  if (!chartData) return <p>Loading chart...</p>;

  return <Bar data={chartData} />;
}

export default EquipmentChart;


