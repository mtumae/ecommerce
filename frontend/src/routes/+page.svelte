<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
  
    interface Product {
      name: string;
      image?: string;
      stock: number;
      // Add other product properties as needed
    }
  
    let productsGrid: HTMLElement;
    let loading = false;
    let errorMessage = '';
    let showError = false;
    let showEmpty = false;
    let products: Product[] = [];
  
    async function fetchProducts() {
      loading = true;
      showError = false;
      showEmpty = false;
      
      try {
        const response = await fetch('https://ecommerce-7o3b.onrender.com/api/products/');
        
        if (!response.ok) {
          throw new Error(`Server responded with status: ${response.status}`);
        }
        
        products = await response.json() as Product[];
        
        if (!products || products.length === 0) {
          showEmpty = true;
        }
      } catch (error: unknown) {
        console.error('Error fetching products:', error);
        errorMessage = error instanceof Error ? error.message : 'Failed to fetch products. Please try again later.';
        showError = true;
      } finally {
        loading = false;
      }
    }
  
    function scrollToProducts() {
      document.getElementById('products-section')?.scrollIntoView({ behavior: 'smooth' });
      fetchProducts();
    }
  
    function navigateToSignIn() {
      goto('/signin');
    }
  
    onMount(() => {
      // Any initialization code can go here
    });
  </script>
  
  <svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  </svelte:head>
  
  <div class="font-['Poppins'] bg-[#f9fafb]">
    <!-- Header -->
    <header class="bg-white shadow-md">
      <div class="container mx-auto px-4 py-4 flex justify-between items-center">
        <div class="flex items-center space-x-2">
          <i class="fas fa-shopping-bag text-blue-600 text-2xl"></i>
          <h1 class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600">Apparel</h1>
        </div>
        <nav class="hidden md:flex space-x-8">
          <a href="/" class="font-medium text-gray-700 hover:text-blue-600 transition-colors">Home</a>
          <a href="/products" class="font-medium text-gray-700 hover:text-blue-600 transition-colors">Products</a>
          <a href="/categories" class="font-medium text-gray-700 hover:text-blue-600 transition-colors">Categories</a>
          <a href="/about" class="font-medium text-gray-700 hover:text-blue-600 transition-colors">About</a>
        </nav>
        <div class="flex items-center space-x-4">
          <button aria-label="Shopping cart - 0 items" class="relative text-gray-700 hover:text-blue-600 transition-colors">
            <i class="fas fa-shopping-cart text-xl"></i>
            <span class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">0</span>
          </button>
          <button 
            on:click={navigateToSignIn}
            class="hidden md:block px-4 py-2 rounded-full bg-blue-50 text-blue-600 font-medium hover:bg-blue-100 transition-colors"
          >
            Sign In
          </button>
          <button aria-label="Open menu" class="md:hidden text-gray-700">
            <i class="fas fa-bars text-xl"></i>
          </button>
        </div>
      </div>
    </header>
  
    <!-- Main Content -->
    <main class="container mx-auto px-4 py-8">
      <!-- Hero Section -->
      <section class="mb-16 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-2xl overflow-hidden">
        <div class="flex flex-col md:flex-row items-center">
          <div class="p-8 md:p-16 flex-1">
            <h2 class="text-4xl md:text-5xl font-bold text-gray-800 mb-4">Discover Premium Products</h2>
            <p class="text-lg text-gray-600 mb-8">Browse our curated collection of high-quality items at competitive prices.</p>
            <button 
              on:click={scrollToProducts}
              class="px-8 py-3 bg-blue-600 text-white rounded-full font-semibold hover:bg-blue-700 transition-colors shadow-lg flex items-center"
            >
              Browse Products
              <i class="fas fa-arrow-right ml-2"></i>
            </button>
          </div>
          <div class="flex-1 relative h-64 md:h-auto">
            <img 
              src="https://images.unsplash.com/photo-1607082349566-187342175e2f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2340&q=80" 
              alt="Premium products" 
              class="object-cover w-full h-full"
            >
          </div>
        </div>
      </section>
  
      <!-- Products Section -->
      <section id="products-section">
        <div class="flex justify-between items-center mb-8">
          <h2 class="text-3xl font-bold text-gray-800">Our Products</h2>
          <div class="flex items-center space-x-4">
            <div class="relative">
              <input type="text" placeholder="Search products..." class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors">
              <i class="fas fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
            </div>
            <div class="relative">
              <select class="appearance-none pl-4 pr-10 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors bg-white">
                <option>All Categories</option>
                <option>Electronics</option>
                <option>Clothing</option>
                <option>Home Goods</option>
              </select>
              <i class="fas fa-chevron-down absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 pointer-events-none"></i>
            </div>
          </div>
        </div>
  
        {#if loading}
          <div class="flex justify-center items-center py-20">
            <div class="loader rounded-full border-4 border-gray-200 h-12 w-12"></div>
          </div>
        {/if}
  
        {#if showError}
          <div class="bg-red-50 border border-red-200 text-red-600 p-4 rounded-lg text-center my-10">
            <i class="fas fa-exclamation-circle mr-2"></i>
            <span>{errorMessage}</span>
          </div>
        {/if}
  
        {#if products.length > 0}
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            {#each products as product}
              <div class="product-card bg-white rounded-xl overflow-hidden shadow-md hover:shadow-xl">
                <div class="relative overflow-hidden h-64">
                  <img src={product.image || 'https://via.placeholder.com/300x300?text=No+Image'} 
                       alt={product.name} 
                       class="w-full h-full object-cover">
                  {#if product.stock <= 0}
                    <div class="absolute top-2 right-2 bg-red-500 text-white text-xs px-2 py-1 rounded-full">
                      Out of Stock
                    </div>
                  {/if}
                </div>
              </div>
            {/each}
          </div>
        {/if}
  
        {#if showEmpty}
          <div class="flex flex-col items-center justify-center py-20">
            <img src="https://cdn-icons-png.flaticon.com/512/1370/1370907.png" alt="Empty cart" class="w-24 h-24 mb-4 opacity-30">
            <h3 class="text-xl font-semibold text-gray-600 mb-2">No products found</h3>
            <p class="text-gray-500 text-center max-w-md">We couldn't find any products matching your criteria. Try adjusting your filters.</p>
          </div>
        {/if}
      </section>
    </main>
  </div>
  
  <style>
    .product-card {
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .product-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }
    .loader {
      border-top-color: #3b82f6;
      animation: spinner 0.6s linear infinite;
    }
    @keyframes spinner {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
  </style>