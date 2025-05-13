<template>
  <q-layout view="hHh lpR fFf">
    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>
          <q-avatar>
            <img
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuHjLX2FhZ6lsmgckCMA5TTk25fs2yU2oqDg&s"
            />
          </q-avatar>
          CICS Thesis Archive
        </q-toolbar-title>
        <q-input
          outlined
          dense
          placeholder="Search..."
          v-model="searchQuery"
          class="q-ml-md bg-white"
          clearable
          @input="onSearch"
        >
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" elevated>
      <q-list>
        <q-item
          clickable
          v-ripple
          :active="isActive('dashboard')"
          active-class="sidebar-active"
          @click="onButtonClick('dashboard')"
        >
          <q-item-section avatar>
            <q-icon name="dashboard" />
          </q-item-section>
          <q-item-section> Dashboard </q-item-section>
        </q-item>

        <q-item
          clickable
          v-ripple
          :active="isActive('register')"
          active-class="sidebar-active"
          @click="onButtonClick('register')"
        >
          <q-item-section avatar>
            <q-icon name="assignment_ind" />
          </q-item-section>
          <q-item-section> Register Thesis </q-item-section>
        </q-item>

        <q-item
          clickable
          v-ripple
          :active="isActive('manage')"
          active-class="sidebar-active"
          @click="onButtonClick('manage')"
        >
          <q-item-section avatar>
            <q-icon name="assignment" />
          </q-item-section>
          <q-item-section> Manage Thesis </q-item-section>
        </q-item>

        <q-item
          clickable
          v-ripple
          :active="isActive('history')"
          active-class="sidebar-active"
          @click="onButtonClick('history')"
        >
          <q-item-section avatar>
            <q-icon name="history" />
          </q-item-section>
          <q-item-section> Logs </q-item-section>
        </q-item>

        <q-item
          clickable
          v-ripple
          :active="isActive('settings')"
          active-class="sidebar-active"
          @click="onButtonClick('settings')"
        >
          <q-item-section avatar>
            <q-icon name="settings" />
          </q-item-section>
          <q-item-section> Settings </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'

export default {
  setup() {
    const leftDrawerOpen = ref(false)
    const router = useRouter()
    const route = useRoute()

    const toggleLeftDrawer = () => {
      leftDrawerOpen.value = !leftDrawerOpen.value
    }

    const onButtonClick = (buttonName) => {
      router.push({ path: `/${buttonName}` })
    }

    // Highlight logic
    const isActive = (buttonName) => {
      // Handles both root and subroutes
      if (buttonName === 'dashboard' && (route.path === '/' || route.path === '/dashboard'))
        return true
      return route.path.startsWith(`/${buttonName}`)
    }

    return {
      leftDrawerOpen,
      toggleLeftDrawer,
      onButtonClick,
      isActive,
    }
  },
}
</script>

<style scoped>
.sidebar-active {
  background: #d0e2fd !important; /* darker blue for better contrast */
  color: #005bb6 !important;
  font-weight: bold;
  border-radius: 8px;
}
</style>
