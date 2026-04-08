<template>
  <div class="app-shell">
    <header class="app-header">
      <nav class="app-nav">
        <RouterLink to="/">Projects</RouterLink>
      </nav>
    </header>

    <main class="app-main">
      <slot />
    </main>
  </div>
</template>

<style scoped>
.app-shell {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  border-bottom: 1px solid #e5e7eb;
  padding: 1rem 1.5rem;
}

.app-nav {
  display: flex;
  gap: 1rem;
}

.app-main {
  flex: 1;
  padding: 1.5rem;
}
</style>
