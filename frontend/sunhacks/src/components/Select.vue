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
                <input v-model="message" placeholder="Enter PIN">
                <a class="button">Go!</a>
            </center>
        </div>
  </section>
</div>  
</template>  

<style>
  @import 'Select.css';
</style>