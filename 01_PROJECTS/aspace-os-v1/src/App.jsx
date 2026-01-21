import React from 'react';
import { Dock } from './components/Dock';
import { Window } from './components/Window';
import { useWindowManager } from './hooks/useWindowManager';

/**
 * A'Space OS V1 - Central Interface
 * Following BMAD-METHOD:
 * - Break: Decoupled components (Dock, Window, Dashboard)
 * - Make: Modular architecture with independent OS definitions
 * - Amplify: Simple state management, fallback to local data
 * - Differentiate: Solarpunk visual design, extensible for V2
 */
function App() {
  const {
    windows,
    openWindow,
    closeWindow,
    minimizeWindow,
    focusWindow,
    updateWindowPosition,
  } = useWindowManager();

  return (
    <div className="w-screen h-screen overflow-hidden relative">
      {/* Background - Solarpunk gradient */}
      <div className="absolute inset-0 bg-gradient-to-br from-sky-100 via-nature-50 to-solar-100" />
      
      {/* Animated background pattern */}
      <div className="absolute inset-0 opacity-10">
        <div className="absolute top-10 left-10 w-64 h-64 bg-solar-400 rounded-full filter blur-3xl animate-pulse" />
        <div className="absolute bottom-20 right-20 w-96 h-96 bg-sky-400 rounded-full filter blur-3xl animate-pulse" style={{ animationDelay: '1s' }} />
        <div className="absolute top-1/2 left-1/2 w-80 h-80 bg-nature-400 rounded-full filter blur-3xl animate-pulse" style={{ animationDelay: '2s' }} />
      </div>

      {/* Windows */}
      {windows.map((window) => (
        <Window
          key={window.id}
          window={window}
          onClose={closeWindow}
          onMinimize={minimizeWindow}
          onFocus={focusWindow}
          onUpdatePosition={updateWindowPosition}
        />
      ))}

      {/* Dock */}
      <Dock onOpenWindow={openWindow} />

      {/* Version Badge */}
      <div className="fixed top-4 right-4 glass px-3 py-1 rounded-lg text-xs font-mono text-gray-600">
        A'Space OS v1.0.0-alpha
      </div>
    </div>
  );
}

export default App;

