import React from 'react'
import Navbaar from '../components/Navbaar'

export default function SearchResults() {
    return (
        <div style={{ backgroundColor: "#9cd1cb" }}>
            <Navbaar />

            <div className='col-md-9 mt-4 d-flex flex-column align-items-center justify-content-center mt-3'>
                <p style={{ fontSize: "large" }}><b>What Are You Interested In Today?</b></p>
                <div className='w-50 d-flex flex-row align-items-center'>
                    <input type="search" placeholder="Search" className='col-md-12' style={{ borderRadius: "20px", border: "none", padding: "10px", backgroundColor: "#f6f2d2" }} />
                    <button className='ps-3 pe-3 pt-2 pb-2 ms-3' style={{ backgroundColor: "#f68349", color: "white", borderRadius: "20px" }} >Search</button>

                </div>
            </div>
            <div className='col-md-12 d-flex flex-row mt-4'>
                <div className='col-md-9'>
                    <div className='container col-md-12 d-flex flex-row align-items-center justify-content-around'>
                        <button className='card col-md-2 rounded' style={{ backgroundColor: "#7aad8c", color: "white" }}>
                            <div className='card-body ps-1 pe-1 py-1'>
                                <p className='m-0 p-0'><small>Lorem Ipsum is simply dummy text.. </small>  </p>
                            </div>
                        </button>

                        <button className='card col-md-2 rounded' style={{ backgroundColor: "#7aad8c", color: "white" }}>
                            <div className='card-body ps-1 pe-1 py-1'>
                                <p className='m-0 p-0'><small>Lorem Ipsum is simply dummy text.. </small>  </p>
                            </div>
                        </button>

                        <button className='card col-md-2 rounded' style={{ backgroundColor: "#7aad8c", color: "white" }}>
                            <div className='card-body ps-1 pe-1 py-1'>
                                <p className='m-0 p-0'><small>Lorem Ipsum is simply dummy text.. </small>  </p>
                            </div>
                        </button>
                        <button className='card col-md-2 rounded' style={{ backgroundColor: "#7aad8c", color: "white" }}>
                            <div className='card-body ps-1 pe-1 py-1'>
                                <p className='m-0 p-0'><small>Lorem Ipsum is simply dummy text.. </small>  </p>
                            </div>
                        </button>

                    </div>

                    {/* VIDEOS */}
                    <div className='container mt-5 d-flex flex-row justify-content-around' style={{ columnGap: "10px" }}>
                        <div style={{ width: "300px" }}>
                            <div className='card mb-2 w-100 rounded' style={{ width: "180px" }}>
                                <iframe src="https://www.youtube.com/embed/tgbNymZ7vqY" className='rounded'>
                                </iframe>
                            </div>
                            <p className='' style={{ fontFamily: "Verdana", fontSize: "14px" }}>Bohemian Rhapsody||Queen || Concert</p>
                        </div>
                        <div style={{ width: "300px" }}>
                            <div className='card mb-2 w-100 rounded' style={{ width: "180px" }}>
                                <iframe src="https://www.youtube.com/embed/tgbNymZ7vqY" className='rounded'>
                                </iframe>
                            </div>
                            <p className='' style={{ fontFamily: "Verdana", fontSize: "14px" }}>Bohemian Rhapsody||Queen || Concert</p>
                        </div>
                        <div style={{ width: "300px" }}>
                            <div className='card mb-2 w-100 rounded' style={{ width: "180px" }}>
                                <iframe src="https://www.youtube.com/embed/tgbNymZ7vqY" className='rounded'>
                                </iframe>
                            </div>
                            <p className='' style={{ fontFamily: "Verdana", fontSize: "14px" }}>Bohemian Rhapsody||Queen || Concert</p>
                        </div>




                    </div>
                </div>

                <div className='col-md-3 pe-2 ps-1'>
                    <div className='card' style={{ backgroundColor: "#7aad8c", color: "white" }}>
                        <div className='card-body'>
                            <div className='d-flex justify-content-center w-100 mb-4'>
                                <h3 style={{ color: "gold" }}>LeaderBoard</h3>
                            </div>
                            <div>
                                <table class="table">
                                    <thead>
                                        <tr style={{ color: "black" }}>
                                            <th scope="col">Rank</th>
                                            <th scope="col">Student Name</th>

                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr style={{ color: "white" }}>
                                            <th scope="row"><img src='https://png.pngtree.com/element_pic/17/09/02/edd30932d1c6075b4c0e302476b03e13.png' width={20} /> </th>
                                            <th scope="row">Rajdeep</th>
                                        </tr>
                                        <tr style={{ color: "white" }}>
                                            <th scope="row"><img src='https://i.pinimg.com/originals/98/ec/c8/98ecc83568ecd89f20fa4e5e47f7fbd4.png' width={20} /> </th>
                                            <th scope="row">Ashish</th>
                                        </tr>
                                        <tr style={{ color: "white" }}>
                                            <th scope="row"><img src='https://w7.pngwing.com/pngs/919/532/png-transparent-bronze-medal-bronze-medal-gold-medal-medal-medal-gold-material-thumbnail.png' width={20} /> </th>
                                            <th scope="row">Pranjal</th>
                                        </tr>
                                        <tr style={{ color: "white" }}>
                                            <th scope="row">4</th>
                                            <th scope="row">Samunder</th>
                                        </tr>

                                    </tbody>
                                </table>
                            </div>

                        </div>

                    </div>
                </div>
            </div>
            {/* FULL SCREEN VIDEO */}
            <div className='py-5 d-flex align-items-center justify-content-center' style={{ height: "100vh" }}>
                <div className='card border w-75' style={{ height: "100%" }}>
                    <div className='card-body'>

                    </div>
                </div>
            </div>


        </div>

    )
}
