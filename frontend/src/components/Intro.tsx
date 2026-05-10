import { useNavigate } from "react-router-dom"

export default function Intro() {
  const navigate = useNavigate()

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white rounded-2xl shadow-md p-8 max-w-md w-full">        
        <h1 className="text-2xl font-bold text-gray-900">
          Hello
        </h1>

        <p className="text-gray-500 mt-2">
          Welcome to Nexus.
        </p>

        <button 
          onClick={() => navigate('/dashboard')}
          className="mt-4 bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700"
        >
          Click me
        </button>
      

      </div>
    </div>
  )
}