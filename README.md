# stable_diffusion_server
A repo for hosting your own Stable Diffusion API with Flask & Docker

## Requirements:
- NVIDIA GPU with CUDA installed & >10GB memory
- Ubunutu 20.04 (this can be adjusted in Dockerfile if you are using a different OS)
- [Huggingface Access Token](https://huggingface.co/settings/tokens)

## To Start the Server:
1. `git clone https://github.com/viral-medialab/stable_diffusion_server.git`
2. In line 34 of the Dockerfile, replace `<TOKEN>` with your [Huggingface Access Token](https://huggingface.co/settings/tokens)
3. `docker build --tag sd_server .`
4. 'docker run -d -p 3000:3000 sd_server'
The server should now be running at http://<your_external_ip>:3000/

## To Generate an Image from Text:
- Pass your prompt as query string ('?prompt=') to the server
- When calling the server from a browser, be sure to replace spaces with '%20'
- Example Prompt: "Impressionist painting of dog wearing party hat."
    - Resulting url: http://<your_external_ip>:3000/?prompt=impressionist%20painting%20of%20dog%20wearing%20party%20hat
    - Wait ~30 sec for image generation and return
    - ![party](https://user-images.githubusercontent.com/17857556/191831210-caaff347-7708-49ee-bd0f-ed11385d0fd2.png)

The foundation of this repo was built by following Lulia Turc's [article](https://towardsdatascience.com/how-to-run-a-stable-diffusion-server-on-google-cloud-platform-gcp-c879357808bf).
