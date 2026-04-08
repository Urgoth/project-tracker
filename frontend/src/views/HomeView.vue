<template>
  <section>
    <h1>Projects</h1>
    <p>This is the placeholder project list page.</p>
    <p><strong>API Base URL:</strong> {{ apiBaseUrl }}</p>

    <ul>
      <li>
        <RouterLink to="/projects/demo-project">Open demo project dashboard</RouterLink>
      </li>
    </ul>
  </section>
</template>

<script setup lang="ts">
import { apiConfig } from '../api/config'

const apiBaseUrl = apiConfig.baseUrl
</script>
