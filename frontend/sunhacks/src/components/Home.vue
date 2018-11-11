<template>  
<div>  
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
                <div class="columns is-centered">
                    <div class="column is-one-fifth">
                        <input v-model="message" placeholder="Enter PIN">
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
            this.$router.push('/select')
            
        }
    }
}
</script>

<style>
  @import 'Home.css';
</style>