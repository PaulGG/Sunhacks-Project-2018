<template>  
<div>  
  <section class="hero is-danger is-bold">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="title">Pick A Restaurant</h2>
      </div>
    </div>
  </section>
  <section class="section">
      <div class="columns">
        <div class="column" v-for="restaurant in restaurants" v-bind:key="restaurant.id">
          <div class="card">
            <p class="title">{{ restaurant.name}}</p>
            <p class='subtitle'>{{ restaurant.created_at.toDateString() }}</p>
            <p><img v-bind:src="restaurant.imgSrc" v-bind:alt="restaurant.name" width="250px" height="250px" style="border-radius: 20px;"/></p>
          </div>
        </div>
      </div>
            <!--
    <div class="container">
      <div class="card" v-for="restaurant in restaurants" v-bind:key="restaurant.id">
        <div class="card-content">
          <p class="title">{{ restaurant.name}}</p>
          <p class='subtitle'>{{ restaurant.created_at.toDateString() }}</p>
          <p><img v-bind:src="restaurant.imgSrc" v-bind:alt="restaurant.name" width="250px" height="250px" style="border-radius: 20px;"/></p>
        </div>
      </div>
    </div>
    -->
  </section>
</div>  
</template>  
<script>
export default {  
  data() {
    return {
      surveys: [{
      id: 1,
      name: 'Dogs',
      created_at: new Date(2017, 12, 1),
      questions: [
        {
          id: 1,
          text: 'What is your favorite dog?',
          choices: [
            { id: 1, text: 'Beagle', selected: 0 },
            { id: 2, text: 'Labrador', selected: 0 },
            { id: 3, text: 'Rottweiler', selected: 0 }]
        }, {
          id: 2,
          text: 'What is your second favorite dog?',
          choices: [
            { id: 5, text: 'Beagle', selected: 0 },
            { id: 6, text: 'Labrador', selected: 0 },
            { id: 7, text: 'Rottweiler', selected: 0 }]
        }]
      }, {
        id: 2,
        name: 'Cars',
        created_at: new Date(2017, 12, 3),
        questions: [
          {
            id: 5,
            text: 'What is your favorite car?',
            choices: [
              { id: 17, text: 'Corvette', selected: 0 },
              { id: 18, text: 'Mustang', selected: 0 },
              { id: 19, text: 'Camaro', selected: 0 }]
          }, {
            id: 6,
            text: 'What is your second favorite car?',
            choices: [
              { id: 21, text: 'Corvette', selected: 0 },
              { id: 22, text: 'Mustang', selected: 0 },
              { id: 23, text: 'Camaro', selected: 0 }]
          }]
      }],
      restaurants: [{
      id: 1,
      name: 'McDonalds',
      created_at: new Date(),
      imgSrc: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/McDonald%27s_Golden_Arches.svg/240px-McDonald%27s_Golden_Arches.svg.png'
      }, {
      id: 2,
      name: 'Taco Bell',
      created_at: new Date(),
      imgSrc: 'https://vignette.wikia.nocookie.net/logopedia/images/b/b3/Taco_Bell_2016.svg/revision/latest/scale-to-width-down/200?cb=20180430111400'
      }, {
      id: 3,
      name: 'Burger King',
      created_at: new Date(),
      imgSrc: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Burger_King_Logo.svg/1024px-Burger_King_Logo.svg.png'
      }]
    }
  }
}
</script>