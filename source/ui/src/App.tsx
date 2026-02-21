import React, { useState } from 'react';
import { Phone, CalendarCheck, Loader2, AlertCircle, CheckCircle2 } from 'lucide-react';

function App() {
  const [phone, setPhone] = useState('');
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState<{ type: 'idle' | 'success' | 'error', message: string }>({ type: 'idle', message: '' });

  const handleCall = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!phone) {
      setStatus({ type: 'error', message: 'Please provide a Phone Number.' });
      return;
    }

    setLoading(true);
    setStatus({ type: 'idle', message: '' });

    try {
      const response = await fetch('/api/voice/call', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          phone_number: phone
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setStatus({ type: 'success', message: 'Call initiated successfully! Please answer your phone.' });
      } else {
        setStatus({ type: 'error', message: data.detail || 'Failed to initiate call.' });
      }
    } catch (err: any) {
      setStatus({ type: 'error', message: err.message || 'Network error occurred.' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="bg-orb orb-1"></div>
      <div className="bg-orb orb-2"></div>
      
      <div className="app-container">
        <div className="glass-card">
          <div className="header">
            <div className="logo-wrapper">
              <CalendarCheck size={32} color="white" />
            </div>
            <h1>Smart Scheduler</h1>
            <p>Connect with our AI voice agent to book your next meeting instantly.</p>
          </div>

          <form onSubmit={handleCall}>
            <div className="input-group">
              <label className="input-label" htmlFor="phone">Phone Number</label>
              <input
                id="phone"
                type="tel"
                className="input-field"
                placeholder="+1 (555) 000-0000"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
                disabled={loading}
              />
              <Phone size={20} className={`input-icon ${phone ? 'active' : ''}`} />
            </div>
            <button 
              type="submit" 
              className="submit-btn"
              disabled={loading || !phone}
            >
              {loading ? (
                <>
                  <Loader2 size={20} className="pulse" />
                  Initiating...
                </>
              ) : (
                <>
                  <Phone size={20} />
                  Request Call
                </>
              )}
            </button>
          </form>

          {status.type !== 'idle' && (
            <div className={`status-message ${status.type === 'error' ? 'status-error' : 'status-success'}`}>
              {status.type === 'error' ? <AlertCircle size={20} /> : <CheckCircle2 size={20} />}
              <span>{status.message}</span>
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default App;
