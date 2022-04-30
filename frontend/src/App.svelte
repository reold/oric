<script lang="ts">
  import "./app.css";

  let currentStage = 0;
  let uploadInput: HTMLElement;

  let uploadedFile: File;
  let contentDetails = { image: null, title: "", publisher: "" };

  const handleUploadFile = (event) => {
    uploadedFile = event.target.files[0];
    currentStage++;

    let imageReader = new FileReader();
    imageReader.readAsDataURL(uploadedFile);
    imageReader.onload = (e) => {
      contentDetails["image"] = e.target.result;
    };
  };

  const handlePublishFile = () => {
    currentStage = -1;

    const formData = new FormData();
    formData.append("file", uploadedFile);
    formData.append("title", contentDetails["title"]);
    formData.append("publisher", contentDetails["publisher"]);

    const options = {
      method: "POST",
      body: formData,
    };

    fetch("http://localhost:8000/api/add", options)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        currentStage = 2;
      })
      .catch((error) => {
        currentStage = 0;
      });
  };
</script>

<main class="w-[100vw] h-[100vh] bg-zinc-900 text-white">
  <div class="bg-zinc-800 w-full h-[25vh] p-2">
    <p class="text-5xl">ORIC - Repository Contribution</p>
  </div>
  <div
    class="h-[1vh] bg-green-400"
    style="width: {(currentStage / 2) * 100}vw"
  />
  <div
    class="w-full h-[70vh] flex flex-col justify-center items-center space-y-5"
  >
    {#if currentStage == 0}
      <!-- choose upload file -->
      <button
        class="bg-zinc-800 ring-2 ring-zinc-500 rounded-md p-4"
        on:click={() => uploadInput.click()}
        ><svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 inline"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM6.293 6.707a1 1 0 010-1.414l3-3a1 1 0 011.414 0l3 3a1 1 0 01-1.414 1.414L11 5.414V13a1 1 0 11-2 0V5.414L7.707 6.707a1 1 0 01-1.414 0z"
            clip-rule="evenodd"
          />
        </svg>Upload file</button
      >
      <input
        type="file"
        accept=".jpg, .jpeg, .png"
        class="hidden"
        on:change={handleUploadFile}
        bind:this={uploadInput}
      />
    {:else if currentStage == 1}
      <!-- edit upload details -->
      {#if contentDetails["image"]}
        <img
          src={contentDetails["image"]}
          alt=""
          class="ring-1 ring-zinc-500 rounded-md w-[90vw] max-h-[40vh]"
        />
        <input
          type="text"
          bind:value={contentDetails["title"]}
          placeholder="title of content"
          class="text-white outline-none rounded-md bg-zinc-900 ring-1 ring-zinc-500 focus:bg-zinc-800 p-1"
        />
        <input
          type="text"
          bind:value={contentDetails["publisher"]}
          placeholder="original publisher"
          class="text-white outline-none rounded-md bg-zinc-900 ring-1 ring-zinc-500 focus:bg-zinc-800 p-1"
          on:keypress={(e) => (e.key == "Enter" ? handlePublishFile() : null)}
        />
        <button
          class="ring-1 ring-zinc-500 bg-zinc-800 rounded-md text-white p-1 hover:bg-zinc-900"
          on:click={handlePublishFile}>upload</button
        >
      {:else}
        loading
      {/if}
    {:else if currentStage == 2}
      <!-- upload success -->
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-20 w-20 text-green-400"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
          clip-rule="evenodd"
        />
      </svg>
      <p>Upload successful!</p>
    {:else if currentStage == -1}
      <!-- loading stage -->
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-10 w-10 text-amber-400 animate-pulse"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          fill-rule="evenodd"
          d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z"
          clip-rule="evenodd"
        />
      </svg>
      <p class="text-xl">waiting</p>
    {/if}
  </div>
  <div class="w-full h-[5vh] bg-zinc-700">
    &copy Copyright Reold. Report errors <a
      class="text-blue-500"
      href="https://twitter.com/redicrafty"
      target="_blank"
      title="redirects to twitter handle">@redicrafty</a
    >.
  </div>
</main>
