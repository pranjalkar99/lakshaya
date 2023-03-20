import React from "react";

import { useContext, createContext, useEffect, useState } from "react";
import {
    GoogleAuthProvider,
    onAuthStateChanged,
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword,
    signInWithPopup

} from "firebase/auth";
import { auth } from "../lib/firebase";

const UserContext = createContext();

export const AuthContextProvider = ({ children }) => {


    const createUser = (email, password) => {
        return createUserWithEmailAndPassword(auth, email, password);
    };

    const loginUser = (email, password) => {
        return signInWithEmailAndPassword(auth, email, password);
    };


    const signInWithGoogle = () => {
        const provider = new GoogleAuthProvider();
        return signInWithPopup(auth, provider);
    };


    return (
        <UserContext.Provider
            value={{

                createUser,
                loginUser,

                signInWithGoogle

            }}
        >
            {children}
        </UserContext.Provider>
    );
};
export const UserAuth = () => {
    return useContext(UserContext);
};
