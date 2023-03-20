import React, { useEffect, useState } from 'react'
import Navbaar from './components/Navbaar'
import axios from 'axios'
import Backdrop from "@mui/material/Backdrop";
import CircularProgress from "@mui/material/CircularProgress";

function SearchResults() {

    const [search, setSearch] = useState('')
    const [searchResults, setSearchResults] = useState([])
    const [loading, setLoading] = useState(false)

    useEffect(() => {
        const videoItems = JSON.parse(localStorage.getItem('videoItems'))
        setSearchResults(videoItems)
    }, [])


    const handleSearch = (e) => {
        setSearch(e.target.value)
    }

    const handleResponseData = (data) => {
        let videoItems = data.items.filter((item) => {
            if (item.id.kind === 'youtube#video') {
                return item
            }
        })

        videoItems = videoItems.slice(0, 3)

        localStorage.setItem('videoItems', JSON.stringify(videoItems))
        setSearchResults(videoItems)

    }

    const handleSubmit = (e) => {
        setLoading(true)
        e.preventDefault()

        axios.post('http://localhost:5000/user/search', {
            query: search,
            max_results: 15,
        }).then((res) => {
            // console.log(res.data)
            handleResponseData(res.data)
        }).catch((err) => {
            console.log(err)
        }).finally(() => {
            setLoading(false)
        })
    }
    

    return (
        <div style={{ height: "100vh", backgroundColor: "#9cd1cb" }}>
            {loading ? (
        <Backdrop
          sx={{ color: "#fff", zIndex: (theme) => theme.zIndex.drawer + 1 }}
          open={true}
        >
          <CircularProgress color="inherit" />
        </Backdrop>
      ) : (
        <>
            <Navbaar />

            <div className='col-md-9 mt-4 d-flex flex-column align-items-center justify-content-center mt-3'>
                <p style={{ fontSize: "large" }}><b>What Are You Interested In Today?</b></p>
                <div className='w-50 d-flex flex-row align-items-center'>
                    <input type="search" placeholder="Search" className='col-md-12' style={{ borderRadius: "20px", border: "none", padding: "10px", backgroundColor: "#f6f2d2" }} 
                        onChange={handleSearch}
                    />
                    <button className='ps-3 pe-3 pt-2 pb-2 ms-3' style={{ backgroundColor: "#f68349", color: "white", borderRadius: "20px" }} 
                        onClick={handleSubmit}
                    >Search</button>

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
                        {
                            searchResults.map((item, index) => {
                                const videoEmbedLink = "https://www.youtube.com/embed/" + item.id.videoId

                        return ( <div style={{ width: "300px" }}>
                            <div className='card mb-2 w-100 rounded' style={{ width: "180px" }}>
                                <iframe src={videoEmbedLink}  className='rounded' title='test'>
                                </iframe>
                            </div>
                            <p className='' style={{ fontFamily: "Verdana", fontSize: "14px" }}>{item.snippet.title}</p>
                        </div>
                        )
                            })
                        }
                        {/* <div style={{ width: "300px" }}>
                            <div className='card mb-2 w-100 rounded' style={{ width: "180px" }}>
                                <iframe src="https://www.youtube.com/embed/tgbNymZ7vqY" className='rounded' title='test'>
                                </iframe>
                            </div>
                            <p className='' style={{ fontFamily: "Verdana", fontSize: "14px" }}>Bohemian Rhapsody||Queen || Concert</p>
                        </div>
                        <div style={{ width: "300px" }}>
                            <div className='card mb-2 w-100 rounded' style={{ width: "180px" }}>
                                <iframe src="https://www.youtube.com/embed/tgbNymZ7vqY" className='rounded' title='test'>
                                </iframe>
                            </div>
                            <p className='' style={{ fontFamily: "Verdana", fontSize: "14px" }}>Bohemian Rhapsody||Queen || Concert</p>
                        </div> */}




                    </div>
                </div>

                <div className='col-md-3'>
                    kuhojk;l
                </div>
            </div>
            </>
      )}


        </div>

    )
}

export default SearchResults