<script>
    let message = '';
    async function fetchFromDjango() {
        try {
            const response = await fetch('https://ecommerce-7o3b.onrender.com/api/example/');
            const data = await response.json();
            message = data.message;  
        } catch (error) {
            console.error('Error:', error);
            message = 'Error fetching data';
        }
    }
</script>

<div class="flex flex-col items-center gap-4 p-6">
    <button 
        class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 
               transition-colors duration-200 shadow-md active:scale-95"
        on:click={fetchFromDjango}
    >
        Rest API
    </button>

    {#if message}
        <p class="text-lg font-medium text-gray-700 bg-gray-100 p-4 rounded-md shadow">
            {message}
        </p>
    {/if}
</div>