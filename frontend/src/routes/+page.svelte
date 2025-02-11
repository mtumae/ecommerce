<script>
    let message = '';

    async function fetchFromDjango() {
        try {
            const response = await fetch('http://localhost:8000/api/example/');
            const data = await response.json();
            message = data.message;  
        } catch (error) {
            console.error('Error:', error);
            message = 'Error fetching data';
        }
    }
</script>

<button class="border-black border-2" on:click={fetchFromDjango}>
    Rest API
</button>


{#if message}
    <p>{message}</p>
{/if}