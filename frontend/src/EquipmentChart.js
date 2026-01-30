import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { useEffect, useState } from "react";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function EquipmentChart() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/equipment/")
      .then((res) => res.json())
      .then((json) => {
        setData(json);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading chart...</p>;
  if (data.length === 0) return <p>No data available</p>;

  const counts = {};
  data.forEach((item) => {
    counts[item.type] = (counts[item.type] || 0) + 1;
  });

  const chartData = {
    labels: Object.keys(counts),
    datasets: [
      {
        label: "Equipment Count",
        data: Object.values(counts),
        backgroundColor: "rgba(54, 162, 235, 0.7)",
      },
    ],
  };

  return (
    <div style={{ width: "600px", margin: "auto" }}>
      <Bar data={chartData} />
    </div>
  );
}

export default EquipmentChart;

