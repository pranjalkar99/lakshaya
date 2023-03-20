// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDY4PnXDJ7GXw8X4xFeVaahsXhcM4RRgfc",
    authDomain: "lakshaya-7d6b8.firebaseapp.com",
    projectId: "lakshaya-7d6b8",
    storageBucket: "lakshaya-7d6b8.appspot.com",
    messagingSenderId: "198037752522",
    appId: "1:198037752522:web:becc19775385756db50233"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export default app;