<template>  
<div>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.1/css/bulma.min.css" rel="stylesheet" />  
    <section class="hero is-danger is-bold is-medium">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="title">Welcome to Give-me-eat.com!</h2>
        <h3 clas="subtitle">Tired of not knowing where to go to eat?  We've got you covered!  Enter your location below and we'll give you some options for where to eat.</h3>
      </div>
    </div>
  </section>
  <section class="section">
        <div class="card">
            <center>
                <p class="title">Enter Location (PIN):</p>
                <div class="columns is-centered is-vcentered">
                    <div class="column is-narrow is-centered">
                        <input v-model="message" placeholder="Enter PIN">
                    </div>
                    <div class="column is-centered">
                        <div class="dropdown is-hoverable">
                            <div class="dropdown-trigger">
                                <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span>Distance</span>
                                <span class="icon is-small">
                                    <i class="fas fa-sort-down" aria-hidden="true"></i>
                                </span>
                                </button>
                            </div>
                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content">
                                    <a class="dropdown-item">
                                        1 mile
                                    </a>
                                    <a class="dropdown-item">
                                        2 miles
                                    </a>
                                    <a class="dropdown-item is-active">
                                        5 miles
                                    </a>
                                    <a class="dropdown-item">
                                        10 miles
                                    </a>
                                    <a class="dropdown-item">
                                        15 miles
                                    </a>
                                    <a class="dropdown-item">
                                        20 miles
                                    </a>
                                    <a class="dropdown-item">
                                        25 miles
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div class="dropdown is-hoverable">
                            <div class="dropdown-trigger">
                                <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span>Price</span>
                                <span class="icon is-small">
                                    <i class="fas fa-sort-down" aria-hidden="true"></i>
                                </span>
                                </button>
                            </div>
                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content">
                                    <a class="dropdown-item is-active">
                                        $
                                    </a>
                                    <a class="dropdown-item">
                                        $$
                                    </a>
                                    <a class="dropdown-item">
                                        $$$
                                    </a>
                                    <a class="dropdown-item">
                                        $$$$
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="column is-one-fifth">
                        <a class="button is-rounded" @click="changePage()">Go!</a>
                    </div>
                </div>
            </center>
        </div>
  </section>
</div>  
</template>  

<script>
export default{
    methods: {
        changePage() {
            // TODOO: CHANGE
            this.$router.push("Select")
        }
    }
}
</script>

<style>
  @import 'Home.css';
  
</style>
