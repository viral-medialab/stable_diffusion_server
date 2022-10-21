import styles from './PromptInput.module.css';
import React, { useState, useRef, useEffect, useMemo } from "react";

export default function PromptInput({}){

    var baseUrl = window.location.origin;

    const [prompt, setPrompt] = useState("");
    const [generatedImageBase64, setGeneratedImageBase64] = useState(
        "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="
      );

    const submitButton = () =>{
        console.log(prompt)

        fetch(baseUrl + "/app/inference", {
            method: "POST",
            mode: "cors",
            cache: "reload",
            credentials: "same-origin", 
            headers: {
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Credentials": "true",
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ prompt: prompt }), 
          }).then((res) => {
            console.log(res)
            setGeneratedImageBase64(res)
          })
        }


    return(
    <form>
        <label>
            Prompt:
            <input type="text" value={prompt} onChange={(e) => setPrompt(e.target.value)} name="prompt" />
        </label>
        <input type="submit" value="Submit" onClick={submitButton}/>
        <img src={generatedImageBase64} />
    </form>
    )
}
