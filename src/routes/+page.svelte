<script>
    import { onMount } from 'svelte';

    let message = 'Carregando';

    onMount(async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/api/hello');
            if (response.ok) {
                const data = await response.json();
                console.log(data)
                message = data.message;
            }
        } catch (error) {
            message = 'Erro: ' + error.message;
        }
    });
</script>

<main>
    <h1>{message}</h1>
    <form action=""></form>
</main>

<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
    }

    h1 {
        color: #ff3e00;
        font-size: 2em;
    }
</style>
