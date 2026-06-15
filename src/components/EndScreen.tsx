import "../modules/Variables"
import { artistKey, trackKey } from "../modules/Variables";

interface Props
{
    currentTrack: {
        artist: string,
        track: string,
        album: string,
        track_id: string
    },
    roundResult: boolean
}

// Refresh the page to get a new song
function refresh()
{
    location.reload();
}

function EndScreen({currentTrack, roundResult}: Props)
{
    const artistName = currentTrack[artistKey];
    const trackName = currentTrack[trackKey];

    return(
        <div>
            <div className="dark-background fit-content margin-top">
                <div className="album-placeholder inline-block"></div>
                <div className="inline-block">
                    <h2 className="middle-vertical-align inline padding-top padding-horizontal">{trackName}</h2>
                    <h4 className="grey-text middle-vertical-align padding-horizontal">{artistName}</h4>
                </div>
            </div>
            <div className="max-width centered">
                {   
                    roundResult
                    ?
                        <>
                            <h3 className="green-text">You won!</h3>
                        </>
                    :
                        <>
                            <h3 className="red-text">You lost!</h3>
                        </>
                }
                <form onSubmit={refresh}>
                    <input className="fancy-button larger-fancy-button blue-background" type="submit" value="Play again?" autoFocus></input>
                </form>
            </div>
        </div>
    )
}

export default EndScreen