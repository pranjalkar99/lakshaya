import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,

  Link
} from 'react-router-dom';
import Home from './pages/Home';
import SearchResults from './pages/SearchResults';
import Quiz from './pages/Quiz';
import Login from './pages/Login';
import SignUp from './pages/SignUp';
import { AuthContextProvider } from './contexts/AuthContext';

function App() {
  return (


    <AuthContextProvider>
      <Router>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/searchresults" element={<SearchResults />} />
          <Route exact path="/quiz" element={<Quiz />} />
          <Route exact path="/login" element={<Login />} />
          <Route exact path="/signup" element={<SignUp />} />
        </Routes>
      </Router>
    </AuthContextProvider>

  );
}

export default App;
