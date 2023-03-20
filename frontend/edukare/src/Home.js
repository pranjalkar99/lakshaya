import React from 'react'

function Home() {
    return (

        <>
            <div style={{ backgroundColor: "#9cd1cb", height: "100vh" }}>
                <div className='w-100 d-flex align-items-center justify-content-between' style={{ height: "80px", filter: "drop-shadow(1px 1px 10px grey)" }}>
                    <div className='col-md-4 d-flex align-items-center justify-content-center' style={{ backgroundColor: "#7aad8c", height: "100%" }}>
                        <h2 style={{ color: "#f6f2d2" }} className="neon"><b>EduKare</b></h2>
                    </div>
                    <div className='col-md-8 d-flex align-items-center justify-content-around' style={{ backgroundColor: "#9fd2ca", height: "100%" }}>
                        <a href='/' className='text-decoration-none'><p className='m-0 ' style={{ fontSize: "20px", color: "#652f05" }}><b >Home</b></p></a>
                        <a href='/' className='text-decoration-none'><p className='m-0' style={{ fontSize: "20px", color: "#652f05" }}><b>About</b></p></a>
                        <a href='/' className='text-decoration-none'><p className='m-0' style={{ fontSize: "20px", color: "#652f05" }}><b>Contact</b></p></a>
                    </div>
                </div>
                <div className='d-flex flex-'>
                    <div className="d-flex flex-column justify-content-between mb-4">
                        <div className='ps-5 pt-5 col-md-9'>
                            <h1 className='mb-3' style={{ color: "#652f05", textAlign: "start" }}>SYNAPSE</h1>
                            <p style={{ textAlign: "start", lineHeight: "1.6rem", fontSize: "large" }}>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>
                            <p style={{ color: "#652f05", textAlign: "start", fontSize: "large" }}>Lorem ipsum dolor</p>
                        </div>

                        <div className='ps-5 pt-5'>
                            <button className='ps-3 pe-3 pt-2 pb-2' style={{ backgroundColor: "#f68349", color: "white", borderRadius: "20px" }} >Start Learning</button>
                        </div>
                    </div>
                    <div className='col-md-6 d-flex  justify-content-center ps-5 pt-5'>
                        <img src='./images/illustration.png' alt='illustration' height={450} />
                    </div>
                </div>
                <div className='col-md-12 mt-4 d-flex align-items-center justify-content-center'>
                    <div className='w-50 d-flex flex-column align-items-center'>
                        <p style={{ fontSize: "large" }}><b>What Are You Interested In Today?</b></p>
                        <input type="search" placeholder="Search" className='col-md-12' style={{ borderRadius: "20px", border: "none", padding: "10px", backgroundColor: "#f6f2d2" }} />
                    </div>
                </div>
            </div>
        </>
    )
}

export default Home