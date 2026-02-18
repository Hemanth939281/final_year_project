import api from "../../api/api";

export default function Upload() {
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);

    await api.post("/upload/", formData);
    alert("Dataset uploaded");
  };

  return <input className="border p-2 rounded-lg" type="file" onChange={handleUpload} />;
}
