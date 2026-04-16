<!-- frontend/src/views/IntegrationCheckView.vue -->
<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { healthCheckHealthGet } from '@/api'

type IntegrationState = 'idle' | 'loading' | 'success' | 'error'

const state = ref<IntegrationState>('idle')
const payload = ref<unknown>(null)
const errorMessage = ref('')

async function load() {
  state.value = 'loading'
  errorMessage.value = ''

  try {
    const response = await healthCheckHealthGet()
    payload.value = response.data
    state.value = 'success'
  } catch (error) {
    errorMessage.value = error instanceof Error ? error.message : 'Unknown request error'
    state.value = 'error'
  }
}

onMounted(load)
</script>

<template>
  <section class="integration-check">
    <h1>Frontend ↔ Backend Integration</h1>

    <p v-if="state === 'loading'">Checking backend connection…</p>

    <div v-else-if="state === 'success'">
      <p>Connection successful.</p>
      <pre>{{ payload }}</pre>
    </div>

    <div v-else-if="state === 'error'">
      <p>Connection failed.</p>
      <pre>{{ errorMessage }}</pre>
    </div>
  </section>
</template>
