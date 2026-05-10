import { useNavigate } from "react-router-dom"

interface Props {
  title: string
  value: string
}

export default function StatsCard({ title, value }: Props) {

  const navigate = useNavigate();

  return (
    <div className="bg-gray-100 rounded-xl shadow p-6">
      <p className="text-gray-500 text-sm">{title}</p>
      <p className="text-2xl font-bold mt-1">{value}</p>

      <span>
        <button 
          onClick={() => navigate('/')}
          className="mt-4 bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700"
        >
          Back to Home
        </button>
      </span>
    </div>
  )
}