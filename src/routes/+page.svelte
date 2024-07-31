<script>
    import { onMount } from 'svelte';

    let salas = [];
    let nomeSala = '';
    let tipo = '';

    onMount(async () => {
        const res = await fetch('http://127.0.0.1:5000/api/salas');
        salas = await res.json();
    });

    async function addSala() {
        const res = await fetch('http://127.0.0.1:5000/api/salas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nomeSala, tipo})
        });

        if (res.ok) {
            const newSala = await res.json();
            salas = [...salas, newSala];
        }
    }
</script>

<main>
    <h1>Salas</h1>

    <form on:submit|preventDefault={addSala}>
        <input placeholder="Nome da Sala" bind:value={nomeSala} />
        <input placeholder="Tipo de Sala" bind:value={tipo} />
        <button type="submit">Adicionar Sala</button>
    </form>

    <ul>
        {#each salas as sala}
            <li>{sala.nomeSala} - {sala.tipo}</li>
        {/each}
    </ul>
</main>
