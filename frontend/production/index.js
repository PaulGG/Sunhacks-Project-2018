var app = new Vue({ 
    el: '#app',
    data: {
        message: 'Hello Vue!',
        options: [
            {name: 'McDonalds', votes: 0},
            {name: 'Taco Bell', votes: 0},
            {name: 'Burger King', votes: 0}
        ]
    },
    methods: {
        voteFor: function(f) {
            f.votes += 1
        }
    }
});
