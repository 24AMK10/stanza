import Navbar from '../components/Navbar/Navbar';

export default function Page() {
    let heading = "NextJS";
    return (
        <>  
            <Navbar heading={heading} />
            <div className="container">
                <center>
                    <h1>This is the Dashboard</h1>
                </center>
            </div>
        </>
    )
}