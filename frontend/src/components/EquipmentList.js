import React, { useEffect, useState } from "react";

function EquipmentList() {
  const [equipment, setEquipment] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/equipment/")
      .then((res) => res.json())
      .then((data) => setEquipment(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <ul>
      {equipment.map((item, index) => (
        <li key={index}>
          {item.name} – {item.type}
        </li>
      ))}
    </ul>
  );
}

export default EquipmentList;
