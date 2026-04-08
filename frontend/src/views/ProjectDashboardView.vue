<template>
  <section>
    <h1>Project Dashboard</h1>
    <p>This is the placeholder dashboard page.</p>
    <p><strong>Project ID:</strong> {{ projectId }}</p>
  </section>
</template>

<script setup lang="ts">
const props = defineProps<{
  projectId: string
}>()

const { projectId } = props
</script>
